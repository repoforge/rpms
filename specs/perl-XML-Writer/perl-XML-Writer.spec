# $Id$
# Authority: dries
# Upstream: David Megginson <david$megginson,com>
# Upstream: Ed Avis <ed$membled,com>
# Upstream: Joseph Walton <joe$kafsemo,org>

### EL6 ships with perl-XML-Writer-0.606-6.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Writer

Summary: Easily generate well-formed, namespace-aware XML
Name: perl-XML-Writer
Version: 0.612
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Writer/

Source: http://search.cpan.org/CPAN/authors/id/J/JO/JOSEPHW/XML-Writer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.006
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.006

%filter_from_requires /^perl*/d
%filter_setup

%description
Easily generate well-formed, namespace-aware XML.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO examples/
%doc %{_mandir}/man3/XML::Writer.3pm*
%dir %{perl_vendorlib}/XML/
#%{perl_vendorlib}/XML/Writer/
%{perl_vendorlib}/XML/Writer.pm

%changelog
* Tue Jul 26 2011 Yury V. Zaytsev <yury@shurup.com> - 0.612-2
- RFX'ed on RHEL6.

* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 0.612-1
- Updated to version 0.612.

* Tue May  4 2010 Christoph Maser <cmr@financial.com> - 0.611-1
- Updated to version 0.611.

* Wed Mar 31 2010 Christoph Maser <cmr@financial.com> - 0.610-1
- Updated to version 0.610.

* Fri Mar 26 2010 Christoph Maser <cmr@financial.com> - 0.607-1
- Updated to version 0.607.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.606-1
- Updated to version 0.606.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 0.604-1
- Updated to release 0.604.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.603-1
- Updated to release 0.603.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.602-1
- Updated to release 0.602.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.601-1
- Updated to release 0.601.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.600-1
- Updated to release 0.600.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.545-1
- Updated to release 0.545.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.530-1
- Updated to release 0.530.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 0.520-1
- Updated to release 0.520.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.510-1
- Initial package.
