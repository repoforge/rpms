# $Id$
# Authority: dag

Summary: Tool for editing and converting subtitles for DivX films
Name: GTKsubtitler
Version: 0.2.4
Release: 0
License: GPL
Group: Applications/Multimedia
#Source1: %{name}.desktop
URL: http://www.gtksubtitler.prv.pl/

Source: http://matrix.kamp.pl/~pawelb/gtksubtitler/download/GTKsubtitler-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel, gnome-libs-devel

%description
Tool for editing and converting subtitles for DivX films. It supports
mergeing, moveing, changeing format of sub-file and converting (to
iso-8859-1/2) divix subtitles.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_datadir}/pixmaps

install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_applnkdir}/Multimedia}
install src/GTKsubtitler $RPM_BUILD_ROOT%{_bindir}/GTKsubtitler
install pixmaps/GTKsubtitler.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/GTKsubtitler.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README SUB_FORMATS
%{_bindir}/*
%{_datadir}/apps/gnome/Multimedia/%{name}.desktop
%{_datadir}/pixmaps/GTKsubtitler.xpm

%changelog
* Mon Sep 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.4-0
- Update to release 0.2.4-0.

* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 0.2.0-0
- Initial package. (using DAR)
