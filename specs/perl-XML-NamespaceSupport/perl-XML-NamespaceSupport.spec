# $Id$
# Authority: dag
# Upstream: Chris Prather <chris@prather.org>

### EL6 ships with perl-XML-NamespaceSupport-1.10-3.el6
%{?el6:# Tag: rfx}
### EL5 ships with perl-XML-NamespaceSupport-1.09-1.2.1
%{?el5:# Tag: rfx}
### EL4 ships with perl-XML-NamespaceSupport-1.08-6
%{?el4:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-NamespaceSupport

Summary: Perl module that implements a simple generic namespace support class
Name: perl-XML-NamespaceSupport
Version: 1.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-NamespaceSupport/

Source: http://search.cpan.org/CPAN/authors/id/P/PE/PERIGRIN/XML-NamespaceSupport-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
perl-XML-NamespaceSupport is a Perl module that implements
a simple generic namespace support class.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"  --skipdeps
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
%doc %{_mandir}/man3/XML::NamespaceSupport.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/NamespaceSupport.pm

%changelog
* Fri Mar 26 2010 Christoph Maser <cmr@financial.com> - 1.11-1
- Updated to version 1.11.

* Wed Jun 17 2009 Christoph Maser <cmr@financial.com> - 1.10-1
- Updated to version 1.10.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Updated to release 1.09.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 1.08-1
- Fixed site -> vendor. (Matthew Mastracci)

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 1.08-0
- Initial package. (using DAR)
