# $Id$
# Authority: dag
# Upstream: Sean M. Burke <sburke$cpan,org>

### EL6 ships with perl-Pod-Spell-1.01-6.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-Spell

Summary: Perl module that implements a formatter for spellchecking Pod
Name: perl-Pod-Spell
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Spell/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-Spell-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Pod-Spell is a Perl module that implements a formatter
for spellchecking Pod.

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
%doc ChangeLog MANIFEST README
%doc %{_mandir}/man3/Pod::Spell.3pm*
%doc %{_mandir}/man3/Pod::Wordlist.3pm.gz
%{_bindir}/podspell
%dir %{perl_vendorlib}/Pod/
#%{perl_vendorlib}/Pod/Spell/
%{perl_vendorlib}/Pod/Spell.pm
%{perl_vendorlib}/Pod/Wordlist.pm
%{perl_vendorlib}/Pod/Wordlist.pod

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
