%global commit 186f37f47c6b339188b010335698a396eddffd71
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name: finalterm
Version: 0.1
Release: 1.git%{shortcommit}%{?dist}
Summary: Final Term is a new breed of terminal emulator.

License: GPL
URL: http://%{name}.org
Source0: https://github.com/p-e-w/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: vala
BuildRequires: cmake >= 2.8
BuildRequires: pkgconfig
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(clutter-1.0) >= 1.12
BuildRequires: pkgconfig(clutter-gtk-1.0)
BuildRequires: pkgconfig(mx-1.0)
BuildRequires: pkgconfig(keybinder-3.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: intltool
BuildRequires: gettext

%description
Final Term is a new breed of terminal emulator.
It goes beyond mere emulation and understands what is happening inside the shell it is hosting.
This allows it to offer features no other terminal can, including:
* Semantic text menus
* Smart command completion
* GUI terminal controls

%prep
%setup -qn %{name}-%{commit}
cmake -DCMAKE_INSTALL_PREFIX=/usr .

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc COPYING README.md
%{_bindir}/finalterm
%{_mandir}/man1/finalterm.1.*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/final-term.*
%{_datadir}/glib-2.0/schemas/org.gnome.finalterm.gschema.xml
%{_datadir}/locale/*/LC_MESSAGES/finalterm.mo

%changelog
* Sat Jun 14 2014 Dmitry Melnichenko 0.1-1.git186f37f
- Initial import based on commit 186f37f47c6b339188b010335698a396eddffd71
