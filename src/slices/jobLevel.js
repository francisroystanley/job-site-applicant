import { createSlice } from "@reduxjs/toolkit";


const jobLevelSlice = createSlice({
  name: 'joblevel',
  initialState: [
    { code: 'FRESHGRAD_ENTRY', name: 'Fresh Graduate' },
    { code: 'RANK_FILE', name: 'Rank and File' },
    { code: 'TECH_STAFF_OFFCR', name: 'Technical Staff / Officer' },
    { code: 'ASSOC_SUPVR', name: 'Supervisor' },
    { code: 'MIDSR_MNGR', name: 'Manager' },
    { code: 'SR_MNGR', name: 'Senior Manager' },
    { code: 'DIR_EXEC', name: 'Executive' }
  ],
  reducers: {}
});

export default jobLevelSlice;
