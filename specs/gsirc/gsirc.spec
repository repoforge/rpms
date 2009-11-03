# $Id$

# Authority: dag

# Soapbox: 0

Summary: lightweight and flexible IRC client for the .NET framework
Name: gsirc
Version: 0.1.1
Release: 0.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.atoker.com/gsirc/

Source: http://www.atoker.com/%{name}/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: mono

BuildArch: noarch

%description
gsirc is a lightweight and flexible IRC client for the .NET framework.
It makes use of Gtk# and is known to run on Linux and on Windows.

It features a handy full-screen mode (Flotilla) which is great for
tracking dozens of IRC channels on a dedicated X terminal or display.

The name stands for gtk-sharp IRC, and isn't related to the original
gsirc that now lies abandoned in GNOME CVS.

%prep
%setup

%build
%{__rm} -f *.exe
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall NAME="%{name}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/*
%{_libdir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.1-0.2
- Rebuild for Fedora Core 5.

* Tue Jan 21 2003 Dag Wieers <dag@wieers.com> - 0.1.1
- Initial package. (using DAR)
