# $Id$
# Authority: dries
# Upstream: Daniel T. Staal <DStaal$usa,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Stream

Summary: HTML output stream class, and some markup utilities
Name: perl-HTML-Stream
Version: 1.60
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Stream/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Stream-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The HTML::Stream module provides you with an object-oriented (and
subclassable) way of outputting HTML. Basically, you open up an "HTML
stream" on an existing filehandle, and then do all of your output to the
HTML stream. You can intermix HTML-stream-output and
ordinary-print-output, if you like.

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
find docs/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST META.yml README README.system docs/ examples/
%doc %{_mandir}/man3/HTML::Stream.3pm*
%dir %{perl_vendorlib}/HTML/
#%{perl_vendorlib}/HTML/Stream/
%{perl_vendorlib}/HTML/Stream.pm

%changelog
* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 1.60-1
- Updated to release 1.60.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.59-1
- Updated to release 1.59.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.55-1
- Initial package.
