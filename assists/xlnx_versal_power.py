# if this bit combination is on for usage offset, the meaning is as described below
req_usage_message = "Device usage policies"
req_usage = {
 0 : "device accessible from all subsystem",
 1 : "device simultaneously shared between two or more subsystems",
 2 : "device exclusively reserved by one subsystem, always",
 3 : "device is time shared between two or more subsystems",
}

usage_mask = 0x3
def usage(flags):
  msg = "# usage: "
  msg += hex(flags)
  msg += " & usage_mask (0x3) --> "
  msg += hex(flags & usage_mask)
  msg += " "
  msg += req_usage[flags & usage_mask]
  return msg

req_security_message = "Device/Memory region security status requirement per TrustZone."
req_security = {
 0 : "Device/Memory region only allows access from secure masters",
 1 : "Device/Memory region allow both secure or non-secure masters",
}
security_mask = 0x4
security_offset = 0x2
def security(flags):
  msg = "# security: ("
  msg += hex(flags)
  msg += " & security_mask(" + hex(security_mask)
  msg += ") ) >> security_offset("
  msg += hex(security_offset)
  msg += ") --> "
  msg += hex((flags & security_mask) >> security_offset)
  msg += " "
  msg += req_security[(flags & security_mask) >> security_offset]
  return msg

# this map is only applicable for memory regions
req_rd_wr_message = "Read/Write access control policy"
req_rd_wr = {
  0 : "Transaction allowed",
  1 : "Transaction not Allowed",
}
rd_policy_mask = 0x8
rd_policy_offset = 0x3
wr_policy_mask = 0x10
wr_policy_offset = 0x4
rw_message = "Read/Write access control policy."
def read_policy(flags):
  msg = "# read policy: ("
  msg += hex(flags)
  msg += " & rd_policy_mask(" + hex(rd_policy_mask)
  msg += ") ) >> rd_policy_offset("
  msg += hex(rd_policy_offset)
  msg += ") --> "
  msg += hex((flags & rd_policy_mask) >> rd_policy_offset)
  msg += " "
  msg += req_rd_wr[(flags & rd_policy_mask) >> rd_policy_offset]
  return msg

def write_policy(flags):
  msg = "# write policy: ("
  msg += hex(flags)
  msg += " & wr_policy_mask(" + hex(wr_policy_mask)
  msg += ") ) >> wr_policy_offset("
  msg += hex(wr_policy_offset)
  msg += ") --> "
  msg += hex((flags & wr_policy_mask) >> wr_policy_offset)
  msg += " "
  msg += req_rd_wr[(flags & wr_policy_mask) >> wr_policy_offset]
  return msg


nsregn_check_mask = 0x20
nsregn_check_offset = 0x5

nsregn_message = "Non-secure memory region check type policy."
nsregn = {
  0 : "RELAXED",
  1: "STRICT",
}

def nsregn_policy(flags):
  msg = "# Non-secure memory region check type policy: ("
  msg += hex(flags)
  msg += " & nsregn_check_mask(" + hex(nsregn_check_mask)
  msg += ") ) >> nsregn_check_offset("
  msg += hex(nsregn_check_offset)
  msg += ") --> "
  msg += hex((flags & nsregn_check_mask) >> nsregn_check_offset)
  msg += " "
  msg += nsregn[(flags & nsregn_check_mask) >> nsregn_check_offset]
  return msg

capability_offset = 0x8
capability_mask = 0x7F00

cap_message = "capability: "
def capability_policy(flags):
  msg = "# Capability policy: ("
  msg += hex(flags)
  msg += " & capability_mask(" + hex(capability_mask)
  msg += ") ) >> capability_offset("
  msg += hex(capability_offset)
  msg += ") --> "
  msg += hex((flags & capability_mask) >> capability_offset)
  return msg

prealloc_offset = 0xf
prealloc_mask = 0x8000

prealloc = {
  0:"prealloc not required",
  1:"prealloc required",
}

prealloc_message = "prealloc policy "
def prealloc_policy(flags):
  msg = "# Preallocation policy: ("
  msg += hex(flags)
  msg += " & prealloc_mask(" + hex(prealloc_mask)
  msg += ") ) >> prealloc_offset("
  msg += hex(prealloc_offset)
  msg += ") --> "
  msg += hex((flags & prealloc_mask) >> prealloc_offset)
  msg += " "
  msg += prealloc[(flags & prealloc_mask) >> prealloc_offset]
  return msg


mailbox_devices = {
  "mailbox@ff320000":"dev_ipi_0",
  "mailbox@ff390000":"dev_ipi_1",
  "mailbox@ff310000":"dev_ipi_2",
  "mailbox@ff330000":"dev_ipi_3",
  "mailbox@ff340000":"dev_ipi_4",
  "mailbox@ff350000":"dev_ipi_5",
  "mailbox@ff360000":"dev_ipi_6",
}

apu_specific_reqs = {
  "dev_l2_bank_0":  0x4,
  "dev_ams_root":   0x4,
  "dev_acpu_0":     0x8104,
  "dev_acpu_1":     0x8104,
}

cpu_subsystem_map = {
  "a72" :       0x1c000003,
  "r5_lockstep":0x1c000004,
  "r5_0":       0x1c000005,
  "r5_1":       0x1c000006,
}

memory_range_to_dev_name = {
 0xffe00000:"dev_tcm_0_a",
 0xffe20000:"dev_tcm_0_a",
 0xffe90000:"dev_tcm_1_a",
 0xffeb0000:"dev_tcm_1_b",
 0x0:"dev_ddr_0",
}

ocm_bank_names = [
  "dev_ocm_bank_0",
  "dev_ocm_bank_1",
  "dev_ocm_bank_2",
  "dev_ocm_bank_3"
]

existing_devices = {
  "dev_rpu0_0":0x18110005 ,
  "dev_rpu0_1":0x18110006 ,
  "dev_ddr_0":0x18320010 ,
  "dev_ocm_bank_0":0x18314007 ,
  "dev_ocm_bank_1":0x18314008 ,
  "dev_ocm_bank_2":0x18314009 ,
  "dev_ocm_bank_3":0x1831400a ,
  "dev_tcm_0_a":0x1831800b ,
  "dev_tcm_0_b":0x1831800c ,
  "dev_tcm_1_a":0x1831800d ,
  "dev_tcm_1_b":0x1831800e ,

  "dev_acpu_0": 0x1810c003,
  "dev_acpu_1" : 0x1810c004 ,
  "dev_ipi_0":0x1822403d ,
  "dev_ipi_1":0x1822403e ,
  "dev_ipi_2":0x1822403f ,
  "dev_ipi_3":0x18224040 ,
  "dev_ipi_4":0x18224041 ,
  "dev_ipi_5":0x18224042 ,
  "dev_ipi_6":0x18224043 ,
  "dev_l2_bank_0": 0x1831c00f,
  "dev_ams_root": 0x18224055,
}

# map xilpm IDs to strings
device_lookup = { 0x1831c00f : "dev_l2_bank_0" ,
  0x18224055 : "dev_ams_root"
}

xilinx_versal_device_names = {
	0x18224018	:   "PM_DEV_USB_0"		,
	0x18224019	:   "PM_DEV_GEM_0"		,
	0x1822401a	:   "PM_DEV_GEM_1"		,
	0x1822401b	:   "PM_DEV_SPI_0"		,
	0x1822401c	:   "PM_DEV_SPI_1"		,
	0x1822401d	:   "PM_DEV_I2C_0"		,
	0x1822401e	:   "PM_DEV_I2C_1"		,
	0x1822401f	:   "PM_DEV_CAN_FD_0"	,
	0x18224020	:   "PM_DEV_CAN_FD_1"	,
	0x18224021	:   "PM_DEV_UART_0"	,	
	0x18224022	:   "PM_DEV_UART_1"	,	
	0x18224023	:   "PM_DEV_GPIO"		,
	0x18224024	:   "PM_DEV_TTC_0"		,
	0x18224025	:   "PM_DEV_TTC_1"		,
	0x18224026	:   "PM_DEV_TTC_2"		,
	0x18224027	:   "PM_DEV_TTC_3"		,
	0x18224029	:   "PM_DEV_SWDT_FPD"	,
	0x1822402a	:   "PM_DEV_OSPI"		,
	0x1822402b	:   "PM_DEV_QSPI"		,
	0x1822402c	:	"PM_DEV_GPIO_PMC"		,
	0x1822402e	:   "PM_DEV_SDIO_0"	,		
	0x1822402f	:   "PM_DEV_SDIO_1"	,		
	0x18224034	:   "PM_DEV_RTC"	,	
	0x18224035	:   "PM_DEV_ADMA_0"	,		
	0x18224036	:   "PM_DEV_ADMA_1"	,		
	0x18224037	:   "PM_DEV_ADMA_2"	,		
	0x18224038	:   "PM_DEV_ADMA_3"	,		
	0x18224039	:   "PM_DEV_ADMA_4"	,		
	0x1822403a	:   "PM_DEV_ADMA_5"	,		
	0x1822403b	:   "PM_DEV_ADMA_6"	,		
	0x1822403c	:   "PM_DEV_ADMA_7"	,		
	0x18224072	:   "PM_DEV_AI"	
}
