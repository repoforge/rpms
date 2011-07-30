# $Id$
# Authority: dag
# Upstream: Martyn J. Pearce <fluffy$cpan,org>

### EL6 ships with perl-Term-ProgressBar-2.09-10.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Term-ProgressBar

Summary: Perl module to provide a progress meter on a standard terminal
Name: perl-Term-ProgressBar
Version: 2.09
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-ProgressBar/

Source: http://www.cpan.org/modules/by-module/Term/Term-ProgressBar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Term-ProgressBar is a Perl module to provide a progress meter
on a standard terminal.

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
%doc BUGS Changes INSTALL MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/Term::ProgressBar.3pm*
%dir %{perl_vendorlib}/Term/
%{perl_vendorlib}/Term/ProgressBar.pm

%changelog
* Tue Jul 26 2011 Yury V. Zaytsev <yury@shurup.com> - 2.09-2
- RFX'ed on RHEL6.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 2.09-1
- Initial package. (using DAR)
