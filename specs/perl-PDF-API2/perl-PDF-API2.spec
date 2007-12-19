# $Id$
# Authority: dag
# Upstream: Alfred Reibenschuh <alfredreibenschuh$gmx,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PDF-API2

Summary: Perl module to faciliate creating and modifying PDF files
Name: perl-PDF-API2
Version: 0.68
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PDF-API2/

Source: http://www.cpan.org/modules/by-module/PDF/PDF-API2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
perl-PDF-API2 is a Perl module to faciliate the creation and modification of
High-Quality "Portable Document Format (aka. PDF)" files.  

%prep
%setup -n %{real_name}-%{version}
# avoid dependency on 'perl(the)' by changing some text
%{__perl} -pi.orig -e 's|use the newer|Use the newer|g;' lib/PDF/API2/Resource/XObject/Image/PNM.pm

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find contrib/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL LICENSE MANIFEST META.yml README TODO VERSION contrib/ examples/
#%doc %{_mandir}/man3/PDF::API2.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/PDF/
%{perl_vendorlib}/PDF/API2/
%{perl_vendorlib}/PDF/API2.pm
%exclude %{perl_vendorlib}/PDF/API2/Basic/TTF/Win32.pm
%exclude %{perl_vendorlib}/PDF/API2/Win32.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.68-1
- Updated to release 0.68.

* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 0.66-1
- Updated to release 0.66.

* Sat Oct 06 2007 Dag Wieers <dag@wieers.com> - 0.65-1
- Initial package. (using DAR)
