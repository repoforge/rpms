# $Id$
# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name LWP-UserAgent-Determined

Summary: Virtual browser that retries errors
Name: perl-LWP-UserAgent-Determined
Version: 1.04
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/LWP-UserAgent-Determined/

Source: http://www.cpan.org/modules/by-module/LWP/LWP-UserAgent-Determined-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This class works just like LWP::UserAgent (and is based on it, by
being a subclass of it), except that when you use it to get a web page
but run into a possibly-temporary error (like a DNS lookup timeout),
it'll wait a few seconds and retry a few times.

It also adds some methods for controlling exactly what errors are
considered retry-worthy and how many times to wait and for how many
seconds, but normally you needn't bother about these, as the default
settings are relatively sane.

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
%doc ChangeLog README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/LWP/
%dir %{perl_vendorlib}/LWP/UserAgent/
%{perl_vendorlib}/LWP/UserAgent/Determined.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.04-1
- Updated to version 1.04.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.03-1.2
- Rebuild for Fedora Core 5.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
