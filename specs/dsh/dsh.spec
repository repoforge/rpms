# $Id$
# Authority: dag
# Upstream: Junichi Uekawa <dancer$netfort,gr,jp>

Summary: Distributed shell. Allows running of a single command on multiple hosts
Name: dsh
Version: 0.23.7
Release: 0.2%{?dist}
Group: System Environment/Shells
License: GPL
URL: http://www.netfort.gr.jp/~dancer/software/dsh.html

Source: http://www.netfort.gr.jp/~dancer/software/downloads/dsh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A distributed shell. Allows running of a single command on multiple hosts.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.23.7-0.2
- Rebuild for Fedora Core 5.

* Thu May 29 2003 Dag Wieers <dag@wieers.com> - 0.23.7-0
- Initial package. (using DAR)
