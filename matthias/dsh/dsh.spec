# Authority: dag
# Upstream: Junichi Uekawa <dancer@netfort.gr.jp>

Summary: A distributed shell. Allows running of a single command on multiple hosts.
Name: dsh
Version: 0.23.7
Release: 0
Group: System Environment/Shells
License: GPL
URL: http://www.netfort.gr.jp/~dancer/software/dsh.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/home-made/apt/

Source: http://www.netfort.gr.jp/~dancer/software/downloads/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

#BuildRequires: 

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
* Thu May 29 2003 Dag Wieers <dag@wieers.com> - 0.23.7-0
- Initial package. (using DAR)
