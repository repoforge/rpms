# $Id$
# Authority: dag
# Upstream: Richard Drummond <info$rcdrummond,net>

Summary: Take screenshots using the framebuffer device
Name: fbdump
Version: 0.4.2
Release: 2%{?dist}
License: GPL
Group: Amusements/Graphics
URL: http://www.rcdrummond.net/fbdump/

Source: http://www.rcdrummond.net/fbdump/fbdump-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
fbdump reads the framebuffer device (/dev/fb*) or a dump thereof and
saves a PPM image file. You can use it for making screenshots of
virtually any application, from traditional text applications to your
X Window System desktop, as well as framebuffer applications.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/fbdump

%changelog
* Fri Mar 09 2007 Dag Wieers <dag@wieers.com> - 0.4.2-2
- Fixed group.

* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Initial package. (using DAR)
