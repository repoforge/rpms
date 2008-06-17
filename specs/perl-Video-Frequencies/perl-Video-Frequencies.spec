# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Video-Frequencies

Summary: Perl interface to the Video4linux tuner frequencies.
Summary: Active Server Pages for Apache with mod_perl
Name: perl-Video-Frequencies
Version: 0.03
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://ivtv.sourceforge.net/

Source: http://dl.sf.net/ivtv/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

%description
This package provides a table of hashes that represent all the current
frequency mappings that are used by Video4Linux programs.

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
%doc Changes COPYING MANIFEST README
%doc %{_mandir}/man3/Video::Frequencies.3pm*
%{perl_vendorlib}/Video/Frequencies.pm

%changelog
* Sun Jun 15 2008 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
