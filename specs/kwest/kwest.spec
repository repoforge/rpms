# $Id$
# Authority: dries
# Upstream: Peter Bienstman <peter,bienstman$ugent,be>

Summary: Interpreter for Infocom and other Z-machine interactive fiction games
Name: kwest
Version: 1.1.1
Release: 1%{?dist}
License: GPL
Group: Applications/Emulators
URL: http://kwest.sourceforge.net/

Source: http://dl.sf.net/kwest/kwest-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gettext, gcc-c++

%description
Kwest is an interpreter for Infocom and other Z-machine interactive fiction 
games. It is based on Frotz and tries to comply with standard 1.0 of Graham 
Nelson's Z-machine specification. Features include a fairly complete Z-machine 
interpreter, support for zblorb files and bibliographic information, support 
for color, styles, and timed input (sound and V6 pictures are not yet 
supported), input-editing facilities such as command history and tab completion
(like Frotz), and more.

%prep
%setup -n %{name}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_docdir}/HTML/en/kwest/
%{_bindir}/kwest
%{_datadir}/applnk/Games/kwest.desktop
%{_datadir}/mimelnk/application/zmachine.desktop
%{_datadir}/apps/kwest/kwestui.rc
%{_datadir}/icons/hicolor/*/*/*.png
%exclude %{_libdir}/lib*.a

%changelog
* Wed Oct  3 2007 Dries Verachtert <dries@ulyssis.org> - 1.1.1-1
- Initial package.
