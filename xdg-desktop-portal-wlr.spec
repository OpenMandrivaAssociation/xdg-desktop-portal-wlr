Name:           xdg-desktop-portal-wlr
Version:        0.7.0
Release:        1
Summary:        xdg-desktop-portal backend for wlroots
License:        MIT
URL:            https://github.com/emersion/xdg-desktop-portal-wlr
Source0:        https://github.com/emersion/xdg-desktop-portal-wlr/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
 
Requires:       dbus
# required for Screenshot portal implementation
Requires:       grim
Requires:       xdg-desktop-portal
# required for Screencast output selection
Recommends:     slurp
Recommends:     wofi
 
Enhances:       sway
Supplements:    (sway and (flatpak or snapd))
 
%description
%{summary}.
This project seeks to add support for the screenshot, screencast, and possibly
remote-desktop xdg-desktop-portal interfaces for wlroots based compositors.
 
 
%prep
%autosetup -p1
 
%build
%meson \
    -Dsd-bus-provider=libsystemd
%meson_build
 
%install
%meson_install
 
%post
%systemd_user_post %{name}.service
 
%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE
%doc README.md contrib/config.sample
%{_libexecdir}/%{name}
%{_mandir}/man5/%{name}.5*
%{_datadir}/xdg-desktop-portal/portals/wlr.portal
%{_datadir}/dbus-1/services/*.service
%{_userunitdir}/%{name}.service
