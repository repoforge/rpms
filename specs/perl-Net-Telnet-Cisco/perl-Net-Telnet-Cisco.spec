# $Id$
# Authority: dries
# Upstream: Joshua Keroes <joshua$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Telnet-Cisco

Summary: Automate Cisco router management
Name: perl-Net-Telnet-Cisco
Version: 1.10
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Telnet-Cisco/

Source: http://search.cpan.org/CPAN/authors/id/J/JO/JOSHUA/Net-Telnet-Cisco-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Net::Telnet::Cisco adds additional functionality to
Net::Telnet that helps you automate Cisco router management
and statistic gathering.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/Telnet/Cisco.pm
%{perl_vendorlib}/auto/Net/Telnet/Cisco

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
