# $Id$
# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Message

Summary: Generic message storage mechanism
Name: perl-Log-Message
Version: 0.01
Release: 2.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Message/

Source: http://www.cpan.org/modules/by-module/Log/Log-Message-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Log::Message is a generic message storage mechanism. It allows you to store
messages on a stack -- either shared or private -- and assign meta-data to
it. Some meta-data will automatically be added for you, like a timestamp and
a stack trace, but some can be filled in by the user, like a tag by which to
identify it or group it, and a level at which to handle the message (for
example, log it, or die with it)
Log::Message also provides a powerfull way of searching through items by
regexes on messages, tags and level.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Log/
%{perl_vendorlib}/Log/Message.pm
%{perl_vendorlib}/Log/Message/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-2.2
- Rebuild for Fedora Core 5.

* Thu Nov 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-2
- Rebuild.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
