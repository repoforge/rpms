# $Id$
# Authority: dag
# Upstream: Alexandre Masselot <alexandre,masselot$genebio,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Util-Properties

Summary: Java.util.properties like class
Name: perl-Util-Properties
Version: 0.18
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Util-Properties/

Source: http://www.cpan.org/authors/id/A/AL/ALEXMASS/Util-Properties-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Digest::MD5::File)

%description
Java.util.properties like class.

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
%doc %{_mandir}/man3/Util::Properties.3pm*
%doc %{_mandir}/man3/Util::Properties::Combine.3pm*
%dir %{perl_vendorlib}/Util/
%{perl_vendorlib}/Util/Properties/
%{perl_vendorlib}/Util/Properties.pm

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.18-1
- Updated to version 0.18.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Wed Dec 05 2007 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Updated to release 0.15.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
