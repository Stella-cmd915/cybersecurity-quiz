import React from 'react';
import { Shield, Lock, Key, AlertTriangle, Fingerprint, Eye, Server, Wifi } from 'lucide-react';
import './AnimatedBackground.css';

const AnimatedBackground = () => {
  const icons = [
    { Icon: Shield, className: 'shield', size: 60, top: '10%', left: '15%' },
    { Icon: Lock, className: 'lock', size: 50, top: '25%', left: '80%' },
    { Icon: Key, className: 'key', size: 45, top: '60%', left: '10%' },
    { Icon: AlertTriangle, className: 'alert', size: 55, top: '70%', left: '85%' },
    { Icon: Fingerprint, className: 'shield', size: 65, top: '15%', left: '60%' },
    { Icon: Eye, className: 'lock', size: 50, top: '45%', left: '75%' },
    { Icon: Server, className: 'key', size: 48, top: '80%', left: '40%' },
    { Icon: Wifi, className: 'alert', size: 52, top: '35%', left: '25%' },
  ];

  const glowOrbs = [
    { className: 'cyan', size: '400px', top: '10%', left: '20%', delay: '0s' },
    { className: 'purple', size: '500px', top: '60%', left: '70%', delay: '3s' },
    { className: 'blue', size: '350px', top: '40%', left: '50%', delay: '6s' },
  ];

  return (
    <div className="animated-background">
      <div className="cyber-grid" />
      
      {glowOrbs.map((orb, index) => (
        <div
          key={`orb-${index}`}
          className={`glow-orb ${orb.className}`}
          style={{
            width: orb.size,
            height: orb.size,
            top: orb.top,
            left: orb.left,
            animationDelay: orb.delay,
          }}
        />
      ))}

      {icons.map((item, index) => {
        const Icon = item.Icon;
        return (
          <Icon
            key={`icon-${index}`}
            className={`floating-icon ${item.className}`}
            size={item.size}
            style={{
              top: item.top,
              left: item.left,
            }}
          />
        );
      })}
    </div>
  );
};

export default AnimatedBackground;