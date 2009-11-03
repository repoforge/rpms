# $Id$
# Authority: dag
# Upstream: Ricardo Signes <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Querylet-Output-Excel-OLE

Summary: Perl module to output query results to Excel via OLE
Name: perl-Querylet-Output-Excel-OLE
Version: 0.142
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Querylet-Output-Excel-OLE/

Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Querylet-Output-Excel-OLE-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Querylet-Output-Excel-OLE is a Perl module to output query results
to Excel via OLE.

This package contains the following Perl module:

    Querylet::Output::Excel::OLE

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Querylet::Output::Excel::OLE.3pm*
%dir %{perl_vendorlib}/Querylet/
%dir %{perl_vendorlib}/Querylet/Output/
%dir %{perl_vendorlib}/Querylet/Output/Excel/
%{perl_vendorlib}/Querylet/Output/Excel/OLE.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.142-1
- Initial package. (using DAR)
