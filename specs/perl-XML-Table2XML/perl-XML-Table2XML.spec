# $Id$
# Authority: dries
# Upstream: Roland Kapl <rkapl$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Table2XML

Summary: Generic conversion of tabular data to XML
Name: perl-XML-Table2XML
Version: 1.4
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Table2XML/

Source: http://www.cpan.org/modules/by-module/XML/XML-Table2XML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Generic conversion of tabular data to XML by reverting Excel's 
flattener methodology.

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
%doc Changes README
%doc %{_mandir}/man3/XML::Table2XML*
%{perl_vendorlib}/XML/Table2XML.pm

%changelog
* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 1.4-1
- Updated to version 1.4.

* Wed May 02 2007 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Updated to release 1.0.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
