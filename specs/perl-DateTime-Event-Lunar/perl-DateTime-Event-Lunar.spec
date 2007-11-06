# $Id$
# Authority: dries
# Upstream: Daisuke Maki <dmaki$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Event-Lunar

Summary: Perl DateTime Extension For Computing Lunar Events
Name: perl-DateTime-Event-Lunar
Version: 0.04
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Event-Lunar/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Event-Lunar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Module::Build)

%description
Perl DateTime Extension For Computing Lunar Events.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib} \
	%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DateTime/Event/Lunar.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1.2
- Rebuild for Fedora Core 5.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
