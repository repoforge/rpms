# $Id$
# Authority: dag

%define real_version 1.0b1

Summary: Graphical Hotline client with almost full 1.5 compatibility
Name: fidelio
Version: 1.0
Release: 0.b1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://fidelio.sourceforge.net/

Source: http://dl.sf.net/fidelio/fidelio-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gnome-libs-devel, libxml-devel, gettext

%description
Fidelio is a Hotline compatible client that supports most of the features of
Hotline. Public chat, tranfsers, flat and threaded news, icons, sounds, and
messages are supported. Banners, private chat, and the administrative
functions are not.

%prep
%setup -n %{name}-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/fidelio.default

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-0.b1.2
- Rebuild for Fedora Core 5.

* Mon Feb 10 2003 Dag Wieers <dag@wieers.com> - 1.0-0.b1
- Initial package. (using DAR)
