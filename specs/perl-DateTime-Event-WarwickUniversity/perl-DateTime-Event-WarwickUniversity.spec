# $Id$
# Authority: dries
# Upstream: Tim Retout <tim$retout,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Event-WarwickUniversity

Summary: Warwick University academic calendar
Name: perl-DateTime-Event-WarwickUniversity
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Event-WarwickUniversity/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Event-WarwickUniversity-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker), perl(Module::Build)

%description
Warwick University academic calendar.

%prep
%setup -n %{real_name}-%{version}

%build
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}
%{__perl} Build.PL
./Build

%install
%{__rm} -rf %{buildroot}
#%{__make} pure_install
PERL_INSTALL_ROOT="%{buildroot}" ./Build install installdirs="vendor"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/DateTime::Event::WarwickUniversity*
%{perl_vendorlib}/DateTime/Event/WarwickUniversity.pm
%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
