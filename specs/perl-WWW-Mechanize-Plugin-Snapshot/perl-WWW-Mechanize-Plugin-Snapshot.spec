# $Id$
# Authority: dries
# Upstream: Joe McMahon <mcmahon$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Mechanize-Plugin-Snapshot

Summary: Snapshot the Mech object's state
Name: perl-WWW-Mechanize-Plugin-Snapshot
Version: 0.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Mechanize-Plugin-Snapshot/

Source: http://search.cpan.org//CPAN/authors/id/M/MC/MCMAHON/WWW-Mechanize-Plugin-Snapshot-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Snapshot the Mech object's state.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/WWW::Mechanize::Plugin::Snapshot*
%{perl_vendorlib}/WWW/Mechanize/Plugin/Snapshot.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Initial package.
