# Authority: dag

Summary: A graphical music notation program.
Name: denemo
Version: 0.7.1
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://denemo.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix} 

%description
Denemo is a graphical music notation program written in C with
gtk+. It is intended to be used in conjunction with GNU Lilypond
(http://www.cs.uu.nl/hanwen/lilypond/), but is adaptable to other
computer-music-related purposes as well. 

%prep
%setup

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
%config %{_datadir}/denemo/denemo.conf
%config %{_datadir}/denemo/*.keymaprc
%dir %{_datadir}/denemo/
%{_datadir}/denemo/pixmaps/
%{_bindir}/*
%{_includedir}/denemo/

%changelog
* Wed Oct 15 2003 Dag Wieers <dag@wieers.com> - 0.7.1-0
- Initial package. (using DAR)
