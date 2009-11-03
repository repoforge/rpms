# $Id$
# Authority: dries
# Upstream: &#21934;&#20013;&#26480; <ken$digitas,harvard,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Tee

Summary: Multiplex output to multiple output handles
Name: perl-IO-Tee
Version: 0.64
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Tee/

Source: http://www.cpan.org/modules/by-module/IO/IO-Tee-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The `IO::Tee' constructor, given a list of output handles, returns a
tied handle that can be written to but not read from. When written to
(using print or printf), it multiplexes the output to the list of
handles originally passed to the constructor. As a shortcut, you can
also directly pass a string or an array reference to the constructor, in
which case `IO::File::new' is called for you with the specified argument
or arguments.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/IO/Tee.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.64-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Initial package.
