# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Socket-INET6

Summary: Object interface for AF_INET|AF_INET6 domain sockets 
Name: perl-IO-Socket-INET6
Version: 2.51
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Socket-INET6/

Source: http://www.cpan.org/modules/by-module/IO/IO-Socket-INET6-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
IO::Socket::INET6 provides an object interface to creating and using sockets
in both AF_INET|AF_INET6 domain. It is built upon the IO::Socket interface and
inherits all the methods defined by IO::Socket.

%prep
%setup -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/IO/
%dir %{perl_vendorlib}/IO/Socket/
%{perl_vendorlib}/IO/Socket/INET6.pm

%changelog
* Wed Mar 30 2005 Dag Wieers <dag@wieers.com> - 2.51-1
- Initial package. (using DAR)
