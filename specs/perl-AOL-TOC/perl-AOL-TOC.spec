# $Id$
# Authority: dag
# Upstream: Joshua Harding <xjharding$elitemail,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AOL-TOC
%define real_version 0.34

Summary: AOL-TOC module for perl
Name: perl-AOL-TOC
Version: 0.340
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AOL-TOC/

Source: http://www.cpan.org/authors/id/J/JH/JHARDING/AOL-TOC-%{version}.tar.gz
#Source: http://www.cpan.org/modules/by-module/AOL/AOL-TOC-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Perl extension for interfacing with AOL's AIM service.

%prep
%setup -n %{real_name}-%{real_version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README README.old
%doc %{_mandir}/man3/AOL::TOC.3pm*
%dir %{perl_vendorlib}/AOL/
%{perl_vendorlib}/AOL/SFLAP.pm
%{perl_vendorlib}/AOL/TOC.pm

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.340-1
- Switch to upstream version.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 0.34-1
- Initial package. (using DAR)
