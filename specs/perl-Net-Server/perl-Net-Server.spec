# $Id$

# Authority: dag

%define rname Net-Server

Summary: Net-Server module for perl 
Name: perl-Net-Server
Version: 0.86
Release: 0
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Server/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://seamons.com/net_server/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Net-Server module for perl

%prep
%setup -n %{rname}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes examples
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Tue Feb 03 2004 Dag Wieers <dag@wieers.com> - 0.86-0
- Updated to release 0.86.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.85-0
- Updated to release 0.85.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 0.84-0
- Initial package. (using DAR)
