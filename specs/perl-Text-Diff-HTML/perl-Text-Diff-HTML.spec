# $Id$
# Authority: dries
# Upstream: David Wheeler <david$kineticode,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Diff-HTML

Summary: XHMTL format for Text::Diff::Unified
Name: perl-Text-Diff-HTML
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Diff-HTML/

Source: http://www.cpan.org/modules/by-module/Text/Text-Diff-HTML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(Module::Build) >= 0.2701
BuildRequires: perl(Test::More) >= 0.17
BuildRequires: perl(Text::Diff)

%description
An XHTML format for Text::Diff::Unified.

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
%doc Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man3/Text::Diff::HTML.3pm*
%dir %{perl_vendorlib}/Text/
%dir %{perl_vendorlib}/Text/Diff/
#%{perl_vendorlib}/Text/Diff/HTML/
%{perl_vendorlib}/Text/Diff/HTML.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
