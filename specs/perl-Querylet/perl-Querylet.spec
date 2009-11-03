# $Id$
# Authority: dag
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Querylet

Summary: Perl module to do simplified queries for the non-programmer
Name: perl-Querylet
Version: 0.324
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Querylet/

Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Querylet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Querylet is a Perl module to do simplified queries for the non-programmer.

This package contains the following Perl modules:

    Querylet
    Querylet::Input
    Querylet::Output
    Querylet::Query

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
%doc %{_mandir}/man3/Querylet.3pm*
%doc %{_mandir}/man3/Querylet::Input.3pm*
%doc %{_mandir}/man3/Querylet::Output.3pm*
%doc %{_mandir}/man3/Querylet::Query.3pm*
%{perl_vendorlib}/Querylet/
%{perl_vendorlib}/Querylet.pm

%changelog
* Mon Jun 22 2009 Christoph Maser <cmr@financial.com> - 0.324-1
- Updated to version 0.324.

* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.323-1
- Initial package. (using DAR)
