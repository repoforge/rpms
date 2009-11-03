# $Id$
# Authority: dag
# Upstream: Piers Harding <piers at cpan dot org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIX-Cal

Summary: Perl wrapper for the original cal UNIX command line tool
Name: perl-UNIX-Cal
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIX-Cal/

Source: http://www.cpan.org/authors/id/P/PI/PIERS/UNIX-Cal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-UNIX-Cal is a Perl wrapper for the original cal UNIX command line tool.

This package contains the following Perl module:

    UNIX::Cal

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/UNIX::Cal.3pm*
%dir %{perl_vendorarch}/UNIX/
%{perl_vendorarch}/UNIX/Cal.pm
%dir %{perl_vendorarch}/auto/UNIX/
%{perl_vendorarch}/auto/UNIX/Cal/

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
