import os

CAR_BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# PLOT.
PLOT_COLORS = {
    "bright_headlight": (250, 128, 114),
    "car": (0, 0, 205),
    "dark_headlight": (205, 201, 201),
    "bright_turn_signal": (238, 130, 238),
    "weak_turn_signal": (139, 137, 137),
    "dark_turn_signal": (216, 191, 216),
    "reflector": (205, 92, 92),
}
FONT_PATH = f"{CAR_BASE_DIR}/resources/simsun.ttc"
FONT_SIZE = int(40.0)
LINE_WIDTH = 2
# SPEED ESTIMATION.
MAX_SMOOTH_LEN_IN_SPEED_ESTIMATION = 9
INIT_SPEED_RATIO = 0.75
SPEED_DEFAULT_INDEX = -1


# system
QUEUE_NAMES = ["detect", "led"]
# ALL_MODELS = [f"{CAR_BASE_DIR}/models/best_20241010.pt", f"{CAR_BASE_DIR}/models/best_20241010_light.pt"]
ALL_MODELS = [f"{CAR_BASE_DIR}/models/best_200_20241114.pt", f"{CAR_BASE_DIR}/models/best_20241010_light.pt"]

DETECTION_TYPES = ["object_detect", "video_class", "img_class", "obb", "light_detect"]
QUERY_STATUS_THRESHOLD = 10
QUEUE_TOSS_TIME_LIMIT = 1000
RAW_FRAME_SKIP = 5
LICENSE_RECOGNIZE_DURATION = 1500


# STATE MACHINE PARAMS
STATE_MACHINE_STATES = ["no_car", "car_arrived", "car_leaving"]
STATE_MACHINE_INVALID_ID = -1
STATE_MACHINE_SPEED_STATIC_LIMIT = 0.0
STATE_MACHINE_SPEED_RUN_LIMIT = 8.0
STATE_MACHINE_SPEED_DEFAULT = -1
STATE_MACHINE_ARRIVE_DELAY_MS = 4000
STATE_MACHINE_LEAVE_DELAY_MS = 10000
STATE_MACHINE_TEMPORAL_LEAVE_DELAY_MS = 3000
STATE_MACHINE_INSPECT_BOX_LEFT_MARGIN = 600
STATE_MACHINE_INSPECT_BOX_RIGHT_MARGIN = 1100
STATE_MACHINE_INSPECT_BOX_TOP_MARGIN = 600
STATE_MACHINE_INSPECT_BOX_BOTTOM_MARGIN = 950
STATE_MACHINE_INSPECT_BOX_FRONT = [[1005, 690], [770, 460]]
STATE_MACHINE_INSPECT_BOX_NOISE = [[50, 35], [30, 22]]

STATE_MACHINE_INSPECT_BOX_BOTTOM_MARGIN_RANGE = [20, 270]
# STATE_MACHINE_INSPECT_BOX_RIGHT_MARGIN_RANGE = [30, 710]
# 不限制车辆靠右侧检车
STATE_MACHINE_INSPECT_BOX_RIGHT_MARGIN_RANGE = [30, 1920]
STATE_MACHINE_INSPECT_POSITION_SLOPE = 0.613
STATE_MACHINE_INSPECT_POSITION_OFFSET_THREAD = -50

STATE_MACHINE_CHECK_LEN = 20

# CAR INSPECT PRECEDURE PARAMS
PRECEDURE_SEQUENCE = [
    ["led_car_strong_light_left", "led_car_strong_light_right"],
    ["led_car_front_turn_light_left", "led_car_back_turn_light_left"],
    ["led_car_front_turn_light_right", "led_car_back_turn_light_right"],
    ["led_car_blink"],
    ["led_car_brake_tail_light"],
]

ALL_SEQUENCE = ["led_car_strong_light_left",
                "led_car_strong_light_right",
                "led_car_front_turn_light_left",
                "led_car_back_turn_light_left",
                "led_car_front_turn_light_right",
                "led_car_back_turn_light_right",
                "led_car_blink",
                "led_car_brake_tail_light"]

PRECEDURE_TOTAL_TIME = 3000  # 30s: -1 IF INFINITE,
PRECEDURE_REMIND_TIMES = 3
# 车辆检测时，单项超时自动通过阈值
PRECEDURE_REMAINS_DELAY_MS = 50*60*1000
GATE_CLOSED = 0
GATE_OPEN = 1
# NOTE: 检测项目间隔，单位毫秒.线下测试可根据测试视频调整
# PRECEDURE_DELT_MS = 5 * 1000
PRECEDURE_DELT_MS = 200
# 全部项目最长检测时间，超时通过，单位毫秒
PRECEDURE_ALL_ITEMS_MAX_TIME_MS = 5 * 60 * 1000

SERVER_ADDRESS = "0.0.0.0"
SERVER_PORT = [18888, 11111, 18889, 18890, 18891]
# SERVER_PORT = [18888]