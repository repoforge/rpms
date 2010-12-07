# $Id$
# Authority: dag
# Upstream: Sullivan Beck <sbeck$cpan,org>

### EL6 ships with perl-Date-Manip-5.54-4.el6
%{?el6:# Tag: rfx}
### EL4 ships with perl-DateManip-5.42a-3
%{?el4:# Tag: rfx}
### EL3 ships with perl-DateManip-5.42a-0.rhel3
%{?el3:# Tag: rfx}
### EL2 ships with perl-DateManip-5.39-5
%{?el2:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Manip

Summary: Date manipulation routines
Name: perl-Date-Manip
Version: 5.56
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Manip/

Source: http://search.cpan.org/CPAN/authors/id/S/SB/SBECK/Date-Manip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(Carp)
BuildRequires: perl(IO::File)
BuildRequires: perl(Module::Build) >= 0.36
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 0:5.6.0
Requires: perl(Carp)
Requires: perl(IO::File)

Obsoletes: perl-DateManip <= %{version}-%{release}
Provides: perl-DateManip = %{version}-%{release}

%description
This is a set of routines designed to make any common date/time manipulation
easy to do. Operations such as comparing two times, calculating a time a given
amount of time from another, or parsing international times are all easily
done. From the very beginning, the main focus of Date::Manip has been to be
able to do ANY desired date/time operation easily, not necessarily quickly.
Also, it is definitely oriented towards the type of operations we (as people)
tend to think of rather than those operations used routinely by computers.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HISTORY INSTALL LICENSE MANIFEST META.yml README README.FIRST TODO examples/
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Date/
%{perl_vendorlib}/Date/Manip/
%{perl_vendorlib}/Date/Manip.pm
%{perl_vendorlib}/Date/Manip.pod

%changelog
* Tue Jun 29 2010 Steve Huff <shuff@vecna.org> - 5.56-1
- Updated to release 5.56.
- Manually specify Perl dependencies.

* Wed Dec 17 2008 Dag Wieers <dag@wieers.com> - 5.48-2
- Provide and obsolete incorrect perl-DateManip.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 5.48-1
- Updated to release 5.48.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 5.46-1
- Initial package. (using DAR)
