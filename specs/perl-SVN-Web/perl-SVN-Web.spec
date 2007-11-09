# $Id$
# Authority: dries
# Upstream: clkao$clkao,org

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVN-Web

Summary: Subversion repository web frontend
Name: perl-SVN-Web
Version: 0.46
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Web/

Source: http://search.cpan.org/CPAN/authors/id/N/NI/NIKC/SVN-Web-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl-Template-Toolkit
BuildRequires: perl-YAML
BuildRequires: perl-XML-RSS
BuildRequires: perl-Text-Diff
BuildRequires: perl-Locale-Maketext-Simple
BuildRequires: subversion-perl
BuildRequires: perl-Text-Diff-HTML
BuildRequires: perl-Template-Plugin-Number-Format
BuildRequires: perl-Locale-Maketext-Lexicon
BuildRequires: perl-Locale-Maketext-Simple
# 0.42 can't be built mod_perl >= 2.0.0
BuildRequires: mod_perl < 2.0.0

%description
SVN::Web is a subversion repository web frontend.

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
%doc README TODO
%doc %{_mandir}/man3/*
%{_bindir}/svnweb-install
%dir %{perl_vendorlib}/SVN/
%{perl_vendorlib}/SVN/Web.pm
%{perl_vendorlib}/SVN/*.pod
%{perl_vendorlib}/SVN/Web/

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.46-1
- Updated to release 0.46.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.42-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Updated to release 0.42.

* Sun Nov  6 2005 Dries Verachtert <dries@ulyssis.org> - 0.40-3
- Added missing perl buildrequirements.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.40-2
- Fixed the source url.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.40-1
- Updated to release 0.40.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Updated to release 0.38.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Initial package.
