# $Id$
# Authority: dries
# Upstream: Ulrich Pfeifer <pfeifer$wait,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Screen

Summary: Extension for easy creation of multi screen CGI scripts
Name: perl-CGI-Screen
Version: 0.122
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Screen/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Screen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
CGI::Screen is a subclass of `CGI' which allows the esay(TM) creation of
simple multi screen CGI scripts. By 'multi screen' I mean scripts which
present different screens to the user when called with different
parameters. This is the common case for scripts linking to themselves.

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
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST README eg/
%doc %{_mandir}/man3/CGI::Screen.3pm*
%dir %{perl_vendorlib}/CGI/
#%{perl_vendorlib}/CGI/Screen/
%{perl_vendorlib}/CGI/Screen.pm

%changelog
* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 0.122-1
- Updated to release 0.122.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.119-1
- Initial package.
