import { BrowserRouter as Router, Routes, Route } from 'react-router';
import LandingPage from '../pages/LandingPage';
import CreateResumePage from '@/pages/CreateResumePage';
import NotFoundPage from '@/pages/NotFoundPage';

export default function AppRoutes() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/create-resume" element={<CreateResumePage />} />
                <Route path="/*" element={<NotFoundPage />} />
            </Routes>
        </Router>
    );
}