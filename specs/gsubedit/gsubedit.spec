# $Id$

# Authority: dag

%define rversion 0.4pre1

Summary: Tool for editing and converting DivX ;-) subtitles.
Name: gsubedit
Version: 0.3.20020604
Release: 0
Group: Applications/Multimedia
License: GPL
URL: http://gsubedit.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gsubedit/gsubedit-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: ORBit-devel, gtk+-devel

%description
GSubEdit, or GNOME Subtitle Editor, is a tool for editing and converting
DivX ;-) subtitles. It currently features read/write of SubRip (.srt)
and MicroDVD (.sub) subtitles. Framerate conversion and frame displacement
(Increase/decrease all frames by a given offset) is also supported.

%prep
%setup -n %{name}-%{rversion}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__rm} -rf %{buildroot}%{_prefix}/doc/

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog README TODO
%doc %{_datadir}/gnome/help/gsubedit/
%{_bindir}/*
%{_datadir}/gnome/apps/Applications/*.desktop
%{_datadir}/pixmaps/gsubedit/

%changelog
* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 0.3.20020604
- Initial package. (using DAR)
