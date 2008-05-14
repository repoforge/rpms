# $Id$
# Authority: dries
# Upstream: John McNamara <plan9$eircom,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name OLE-Storage_Lite

Summary: Read and write OLE storage files
Name: perl-OLE-Storage_Lite
Version: 0.17
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/OLE-Storage_Lite/

Source: http://www.cpan.org/modules/by-module/OLE/OLE-Storage_Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Read and write OLE storage files.

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
%doc %{_mandir}/man3/OLE::Storage_Lite.3pm*
%dir %{perl_vendorlib}/OLE/
#%{perl_vendorlib}/OLE/Storage_Lite/
%{perl_vendorlib}/OLE/Storage_Lite.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Updated to release 0.15.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.
