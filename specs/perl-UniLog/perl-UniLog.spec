# $Id$
# Authority: dag
# Upstream: Daniel Podolsky <tpaba$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UniLog

Summary: Perl module for unified logging on Unix and Win32
Name: perl-UniLog
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UniLog/

Source: http://www.cpan.org/authors/id/T/TP/TPABA/UniLog/UniLog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-UniLog is a Perl module for unified logging on Unix and Win32.

This package contains the following Perl module:

    UniLog

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/UniLog.3pm*
#%{perl_vendorlib}/UniLog/
%{perl_vendorlib}/UniLog.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Initial package. (using DAR)
