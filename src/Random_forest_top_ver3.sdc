# Random Forest Top Level SDC File
# Simple timing constraints for random_forest_top_ver3 design

# Set clock period and port
set ::env(CLOCK_PERIOD) "10.0"
set ::env(CLOCK_PORT) "clk"

# Create clock
create_clock -name clk -period 10.0 [get_ports clk]

# Input delays
set_input_delay -clock clk 1 [get_ports {arbitration_id[*]}]
set_input_delay -clock clk 1 [get_ports {timestamp[*]}]
set_input_delay -clock clk 1 [get_ports {data_field[*]}]
set_input_delay -clock clk 1 [get_ports {feature_valid}]
set_input_delay -clock clk 1 [get_ports {rst_n}]

# Output delays
set_output_delay -clock clk 1 [get_ports {ready_for_next}]
set_output_delay -clock clk 1 [get_ports {prediction_valid}]
set_output_delay -clock clk 1 [get_ports {prediction_out}]
set_output_delay -clock clk 1 [get_ports {frame_id_out[*]}]

# Basic load and driving cell settings
set_driving_cell -lib_cell sky130_fd_sc_hd__buf_1 [get_ports {clk arbitration_id* timestamp* data_field* feature_valid rst_n}]
set_load 0.1 [get_ports {ready_for_next prediction_valid prediction_out frame_id_out*}]