# $Id$
# Authority: dries
# Upstream: Roland Kapl <rkapl$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Table2XML

Summary: Generic conversion of tabular data to XML
Name: perl-XML-Table2XML
Version: 1.0
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Table2XML/

Source: http://search.cpan.org/CPAN/authors/id/R/RK/RKAPL/XML-Table2XML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/XML::Table2XML*
%{perl_vendorlib}/XML/Table2XML.pm

%changelog
* Wed May 02 2007 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Updated to release 1.0.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
