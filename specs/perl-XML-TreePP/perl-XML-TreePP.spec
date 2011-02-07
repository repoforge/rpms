# $Id$
# Authority: dag
# Upstream: Yusuke Kawasaki <u-suke$kawa,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-TreePP

Summary: Pure Perl implementation for parsing/writing xml files
Name: perl-XML-TreePP
Version: 0.41
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-TreePP/

Source: http://search.cpan.org/CPAN/authors/id/K/KA/KAWASAKI/XML-TreePP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl, perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP) >= 5.802
BuildRequires: perl(Test::More)
Requires: perl(LWP) >= 5.802
Requires: perl(Test::More)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description
Pure Perl implementation for parsing/writing xml files.

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

### Clean up docs
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README example/
%doc %{_mandir}/man3/XML::TreePP.3pm*
%dir %{perl_vendorlib}/XML/
#%{perl_vendorlib}/XML/TreePP/
%{perl_vendorlib}/XML/TreePP.pm

%changelog
* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 0.41-1
- Updated to version 0.41.

* Wed Jul  1 2009 Christoph Maser <cmr@financial.com> - 0.39-1
- Updated to version 0.39.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.38-1
- Updated to version 0.38.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.33-1
- Updated to release 0.33.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.32-1
- Initial package. (using DAR)
