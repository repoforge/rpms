# $Id$
# Authority: dag
# Upstream: Ken Prows <perl$xev,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Locale-PO

Summary: Perl module for manipulating .po entries from GNU gettext
Name: perl-Locale-PO
Version: 0.21
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Locale-PO/

Source: http://www.cpan.org/modules/by-module/Locale/Locale-PO-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Locale-PO is a Perl module for manipulating .po entries from GNU gettext.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Locale::PO.3pm*
%dir %{perl_vendorlib}/Locale/
#%{perl_vendorlib}/Locale/PO/
%{perl_vendorlib}/Locale/PO.pm

%changelog
* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 0.21-1
- Updated to release 0.21.

* Sat May 10 2008 Dag Wieers <dag@wieers.com> - 0.20-1
- Updated to release 0.20.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.17-1
- Initial package. (using DAR)
