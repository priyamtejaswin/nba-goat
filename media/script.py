import numpy as np
import pandas as pd
import ipdb
import cPickle as pickle
import matplotlib.pyplot as plt
plt.style.use("ggplot")

import mpld3
from mpld3 import plugins
from mpld3.utils import get_id


### My plotting code.
xw, yw = pickle.load(open("media/xw.cpkl")), pickle.load(open("media/yw.cpkl"))
xb, yb = pickle.load(open("media/xb.cpkl")), pickle.load(open("media/yb.cpkl"))
labels = ["GSW", "CHI"]

fig = plt.figure(figsize=(13, 10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

l1 = ax1.plot(xw, yw, lw=2,)
xsamples = range(0, len(xw), 100)
s1 = ax2.plot(np.array(xw)[xsamples], np.array(yw)[xsamples], 'o', ms=8, )

l1.extend(ax1.plot(xb, yb, lw=2,))
xsamples = range(0, len(xb), 100)
s1.extend(ax2.plot(np.array(xb)[xsamples], np.array(yb)[xsamples], 'o', ms=8, ))

### Their plotting code.
# N_paths = 5
# N_steps = 100
#
# x = np.linspace(0, 10, 100)
# y = 0.1 * (np.random.random((N_paths, N_steps)) - 0.5)
# y = y.cumsum(1)
#
#
# fig = plt.figure()
# ax1 = fig.add_subplot(2,1,1)
# ax2 = fig.add_subplot(2,1,2)
#
# labels = ["a", "b", "c", "d", "e"]
# l1 = ax1.plot(x, y.T, marker='x',lw=2, alpha=0.1)
# s1 = ax2.plot(x, y.T, 'o', ms=8, alpha=0.1)

ipdb.set_trace()

ilp = plugins.InteractiveLegendPlugin(zip(l1, s1), labels)

ilp.JAVASCRIPT = """
    mpld3.register_plugin("interactive_legend", InteractiveLegend);
    InteractiveLegend.prototype = Object.create(mpld3.Plugin.prototype);
    InteractiveLegend.prototype.constructor = InteractiveLegend;
    InteractiveLegend.prototype.requiredProps = ["element_ids", "labels"];
    InteractiveLegend.prototype.defaultProps = {"ax":null,
                                                "alpha_unsel":0.2,
                                                "alpha_over":1.0,
                                                "start_visible":true}
    function InteractiveLegend(fig, props){
        mpld3.Plugin.call(this, fig, props);
    };
    InteractiveLegend.prototype.draw = function(){
        var alpha_unsel = this.props.alpha_unsel;
        var alpha_over = this.props.alpha_over;
        var legendItems = new Array();
        for(var i=0; i<this.props.labels.length; i++){
            var obj = {};
            console.log("HELLO THERE");

            setTimeout(function(){debugger;}, 3000);

            obj.label = this.props.labels[i];
            var element_id = this.props.element_ids[i];
            mpld3_elements = [];


		    debugger;


            for(var j=0; j<element_id.length; j++){
                var mpld3_element = mpld3.get_element(element_id[j], this.fig);
                // mpld3_element might be null in case of Line2D instances
                // for we pass the id for both the line and the markers. Either
                // one might not exist on the D3 side
                if(mpld3_element){
                    mpld3_elements.push(mpld3_element);
                }
            }
            obj.mpld3_elements = mpld3_elements;
            obj.visible = this.props.start_visible[i]; // should become be setable from python side
            legendItems.push(obj);
            set_alphas(obj, false);
        }
        // determine the axes with which this legend is associated
        var ax = this.props.ax
        if(!ax){
            ax = this.fig.axes[0];
        } else{
            ax = mpld3.get_element(ax, this.fig);
        }
        // add a legend group to the canvas of the figure
        var legend = this.fig.canvas.append("svg:g")
                               .attr("class", "legend");
        // add the rectangles
        legend.selectAll("rect")
                .data(legendItems)
                .enter().append("rect")
                .attr("height", 10)
                .attr("width", 25)
                .attr("x", ax.width + ax.position[0] + 25)
                .attr("y",function(d,i) {
                           return ax.position[1] + i * 25 + 10;})
                .attr("stroke", get_color)
                .attr("class", "legend-box")
                .style("fill", function(d, i) {
                           return d.visible ? get_color(d) : "white";})
                .on("click", click).on('mouseover', over).on('mouseout', out);
        // add the labels
        legend.selectAll("text")
              .data(legendItems)
              .enter().append("text")
              .attr("x", function (d) {
                           return ax.width + ax.position[0] + 25 + 40;})
              .attr("y", function(d,i) {
                           return ax.position[1] + i * 25 + 10 + 10 - 1;})
              .text(function(d) { return d.label });
        // specify the action on click
        function click(d,i){
            d.visible = !d.visible;
            d3.select(this)
              .style("fill",function(d, i) {
                return d.visible ? get_color(d) : "white";
              })
            set_alphas(d, false);
        };
        // specify the action on legend overlay
        function over(d,i){
             set_alphas(d, true);
        };
        // specify the action on legend overlay
        function out(d,i){
             set_alphas(d, false);
        };
        // helper function for setting alphas
        function set_alphas(d, is_over){
            for(var i=0; i<d.mpld3_elements.length; i++){
                var type = d.mpld3_elements[i].constructor.name;
                if(type =="mpld3_Line"){
                    var current_alpha = d.mpld3_elements[i].props.alpha;
                    var current_alpha_unsel = current_alpha * alpha_unsel;
                    var current_alpha_over = current_alpha * alpha_over;
                    d3.select(d.mpld3_elements[i].path[0][0])
                        .style("stroke-opacity", is_over ? current_alpha_over :
                                                (d.visible ? current_alpha : current_alpha_unsel))
                        .style("stroke-width", is_over ?
                                alpha_over * d.mpld3_elements[i].props.edgewidth : d.mpld3_elements[i].props.edgewidth);
                } else if((type=="mpld3_PathCollection")||
                         (type=="mpld3_Markers")){
                    var current_alpha = d.mpld3_elements[i].props.alphas[0];
                    var current_alpha_unsel = current_alpha * alpha_unsel;
                    var current_alpha_over = current_alpha * alpha_over;
                    d3.selectAll(d.mpld3_elements[i].pathsobj[0])
                        .style("stroke-opacity", is_over ? current_alpha_over :
                                                (d.visible ? current_alpha : current_alpha_unsel))
                        .style("fill-opacity", is_over ? current_alpha_over :
                                                (d.visible ? current_alpha : current_alpha_unsel));
                } else{
                    console.log(type + " not yet supported");
                }
            }
        };
        // helper function for determining the color of the rectangles
        function get_color(d){
            var type = d.mpld3_elements[0].constructor.name;
            var color = "black";
            if(type =="mpld3_Line"){
                color = d.mpld3_elements[0].props.edgecolor;
            } else if((type=="mpld3_PathCollection")||
                      (type=="mpld3_Markers")){
                color = d.mpld3_elements[0].props.facecolors[0];
            } else{
                console.log(type + " not yet supported");
            }
            return color;
        };
    };
    """

plugins.connect(fig, ilp)
#mpld3.display()
mpld3.show()
