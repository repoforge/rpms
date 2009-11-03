# $Id$

# Authority: dag

Summary: Figaro's password manager
Name: fpm
Version: 0.59
Release: 0.2%{?dist}
License: GPL
Group: Applications/System
URL: http://fpm.sourceforge.net/

Source: http://dl.sf.net/fpm/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk+-devel >= 1.2, gnome-libs-devel

%description
Figaro's Password Manager is a program that allows you to securely store the
passwords you use on the web.  Features include:
- Passwords are encrypted with the blowfish algorithm
- Copy passwords or usernames to the clipboard
- Copy passwords or usernames to the primary selection. (And paste them with a
  middle mouse button click)
- If the password is for a web site, FPM can keep track of the URLs of your
  login screens and can automatically launch your browser.  In this capacity,
  FPM acts as a kind of bookmark manager.
- Combine all three features: you can configure FPM to bring you to a web
  login screen, copy your username to the clipboard and your password to the
  primary selection, all with a single button click.
- FPM also has a passord generator that can choose passwords for you.  It
  allows you to determine how long the password should be, and what types of
  characters (lower case, upper case, numbers and symbols) should be used.
  You can even have it avoid ambiguous characters such as a capital O or the
  number zero.

%prep
%setup

%build
./autogen.sh \
	--prefix="%{_prefix}"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/pixmaps/fpm/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.59-0.2
- Rebuild for Fedora Core 5.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 0.59-0
- Initial package. (using DAR)
