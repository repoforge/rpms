# $Id$
# Authority: dag
# Upstream: Sean M. Burke <sburke$cpan,org>

### EL6 ships with perl-Text-Unidecode-0.04-7.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Unidecode

Summary: Perl module implements an US-ASCII transliterations of Unicode text
Name: perl-Text-Unidecode
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Unidecode/

Source: http://www.cpan.org/modules/by-module/Text/Text-Unidecode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Text-Unidecode is a Perl module implements an US-ASCII
transliterations of Unicode text.

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
%doc ChangeLog MANIFEST MANIFEST.SKIP README TODO.txt TODO.txt
%doc %{_mandir}/man3/Text::Unidecode.3pm*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/Unidecode/
%{perl_vendorlib}/Text/Unidecode.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
