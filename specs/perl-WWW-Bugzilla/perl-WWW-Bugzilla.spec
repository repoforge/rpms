# $Id$
# Authority: dag
# Upstream: Brian Caswell <bmc$shmoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Bugzilla

Summary: Perl module handles submission/update of bugzilla bugs via WWW::Mechanize
Name: perl-WWW-Bugzilla
Version: 1.3
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Bugzilla/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Bugzilla-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-WWW-Bugzilla is a Perl module handles submission/update of bugzilla bugs
via WWW::Mechanize.

%prep
%setup -n %{real_name}-%{version}

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
%doc ARTISTIC Changes MANIFEST META.yml README
%doc %{_mandir}/man3/WWW::Bugzilla.3pm*
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/Bugzilla/
%{perl_vendorlib}/WWW/Bugzilla.pm

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.9-1
- Initial package. (using DAR)
