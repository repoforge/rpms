# $Id$

# Authority: dag

%define rversion 0.7.2a

Summary: Graphical music notation program.
Name: denemo
Version: 0.7.2
Release: 0.a
License: GPL
Group: Applications/Multimedia
URL: http://denemo.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/denemo/denemo-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix} 

%description
Denemo is a graphical music notation program written in C with
gtk+. It is intended to be used in conjunction with GNU Lilypond
(http://www.cs.uu.nl/hanwen/lilypond/), but is adaptable to other
computer-music-related purposes as well. 

%prep
%setup -n %{name}-%{rversion}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING DESIGN GOALS NEWS README TODO
%config(noreplace) %{_datadir}/denemo/denemo.conf
%config %{_datadir}/denemo/*.keymaprc
%dir %{_datadir}/denemo/
%{_datadir}/denemo/pixmaps/
%{_bindir}/*
%{_includedir}/denemo/

%changelog
* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 0.7.2-0.a
- Updated to release 0.7.2a.

* Wed Oct 15 2003 Dag Wieers <dag@wieers.com> - 0.7.1-0
- Initial package. (using DAR)
